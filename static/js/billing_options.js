document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const projectName = formData.get('project_name');
        const projectDescription = formData.get('project_description');
        const billingOption = formData.get('billing_option');

        const data = {
            option_type: billingOption,
            data: {
                project_name: projectName,
                project_description: projectDescription
            }
        };

        fetch(`/billing/${projectName}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Billing option set successfully');
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred while setting the billing option');
        });
    });
});