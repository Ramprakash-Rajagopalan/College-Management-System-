// Handle form submission for adding students
const form = document.getElementById('studentForm');

if(form) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const student = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            department: document.getElementById('department').value,
            year: document.getElementById('year').value
        };

        try {
            const response = await fetch('/students', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(student)
            });

            const data = await response.json();

            if(response.ok) {
                showAlert('Student Added Successfully!', 'success');
                form.reset();
                setTimeout(() => {
                    window.location.href = '/students-page';
                }, 1500);
            } else {
                showAlert(data.error || 'Error adding student', 'error');
            }
        } catch(error) {
            showAlert('Error: ' + error.message, 'error');
        }
    });
}

// Load and display all students
const studentTable = document.getElementById('studentTable');

if(studentTable) {
    loadStudents();
}

async function loadStudents() {
    try {
        const response = await fetch('/students');
        const data = await response.json();

        const tbody = document.getElementById('studentTable');
        tbody.innerHTML = '';

        if(data.length === 0) {
            tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#999;">No students found</td></tr>';
            return;
        }

        data.forEach(student => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${student.id}</td>
                <td>${student.name}</td>
                <td>${student.email}</td>
                <td>${student.department}</td>
                <td>${student.year}</td>
                <td>
                    <div class="action-buttons">
                        <button class="btn-edit" onclick="editStudent(${student.id})">Edit</button>
                        <button class="btn-delete" onclick="deleteStudent(${student.id})">Delete</button>
                    </div>
                </td>
            `;
            tbody.appendChild(row);
        });
    } catch(error) {
        console.error('Error loading students:', error);
        showAlert('Error loading students: ' + error.message, 'error');
    }
}

// Edit student
async function editStudent(studentId) {
    try {
        const response = await fetch(`/students/${studentId}`);
        const student = await response.json();

        if(student.error) {
            showAlert('Student not found', 'error');
            return;
        }

        const newName = prompt('New Name:', student.name);
        if(newName === null) return;

        const newEmail = prompt('New Email:', student.email);
        if(newEmail === null) return;

        const newDepartment = prompt('New Department:', student.department);
        if(newDepartment === null) return;

        const newYear = prompt('New Year:', student.year);
        if(newYear === null) return;

        const updateResponse = await fetch(`/students/${studentId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: newName,
                email: newEmail,
                department: newDepartment,
                year: newYear
            })
        });

        const updateData = await updateResponse.json();

        if(updateResponse.ok) {
            showAlert('Student Updated Successfully!', 'success');
            loadStudents();
        } else {
            showAlert(updateData.error || 'Error updating student', 'error');
        }
    } catch(error) {
        showAlert('Error: ' + error.message, 'error');
    }
}

// Delete student
async function deleteStudent(studentId) {
    if(!confirm('Are you sure you want to delete this student?')) {
        return;
    }

    try {
        const response = await fetch(`/students/${studentId}`, {
            method: 'DELETE'
        });

        const data = await response.json();

        if(response.ok) {
            showAlert('Student Deleted Successfully!', 'success');
            loadStudents();
        } else {
            showAlert(data.error || 'Error deleting student', 'error');
        }
    } catch(error) {
        showAlert('Error: ' + error.message, 'error');
    }
}

// Show alert messages
function showAlert(message, type) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);

    setTimeout(() => {
        alertDiv.remove();
    }, 3000);
}

            studentTable.innerHTML += `

                <tr>
                    <td>${student.id}</td>
                    <td>${student.name}</td>
                    <td>${student.email}</td>
                    <td>${student.department}</td>
                    <td>${student.year}</td>
                </tr>

            `;
        });

    });

}
