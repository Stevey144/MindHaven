
$(document).ready(function() {

        // jQuery click event for the button
        $('#btn-submit-form').on('click', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Get the email and password values
            var user_email = $('#Email').val();
            var user_password = $('#Password').val();    
            var FirstName = $('#FirstName').val();
            var last = $('#last').val();

            // Basic validation to check if email and password are provided
            if (user_email === '' || user_password === '' || FirstName == '' || last === '') {
                alert('all fields are required.');
                return; // Stop if validation fails
            }

            // Store the email and password in localStorage
            localStorage.setItem('email', user_email);
            localStorage.setItem('password', user_password);

            alert("Success! please proceed to sign in page to continue.");

            // Redirect to appointment.html with a timestamp
            window.location.href = "appointment.html?timestamp=" + new Date().getTime();
        });





        $('#btn-sign-in').on('click', function(event) {
                event.preventDefault(); // Prevent default form submission
        
        var user_email;
        var user_password;
        
        var get_Local_Storage_email;
        var get_Local_Stroage_password;
        
        
        var user_email = $('#Email').val();
        var user_password = $('#Password').val();
        
        
        get_Local_Storage_email = localStorage.getItem('email');
        get_Local_Stroage_password = localStorage.getItem('password');
        
        if(!get_Local_Storage_email || !get_Local_Stroage_password){
                alert("No such record found in database");
        }
        
        if(user_email.toString() == get_Local_Storage_email.toString() && user_password == get_Local_Stroage_password){
                window.location.href = "booking.html?timestamp=" + new Date().getTime();
                alert("Login Successful, continue to Book Appointment!");
        }
        else{
                alert("Invalid user details");
        }
        
        
        });


        $('#reach-out').on('click', function(event) {
                event.preventDefault(); // Prevent default form submission
                var firstname = $('#FirstName').val();
                var lastname = $('#last').val();
                var gender = $('#gender-type').val();
                var disability = $('#disability').val();
                var address = $('#address').val();
                var mobile_number = $('#phonenumber').val();

                if(firstname && lastname && gender && disability && address && mobile_number){
                alert("Yaayy!!  Thank you " + firstname + " " + lastname + " for contacting us, Our representative will get back to you on the mobile number you provided which is " + mobile_number);
                location.reload();
                }
                else{
                        alert("all field marked with * are required");
                }

         });



        $('#btn-booking').on('click', function(event) {
                event.preventDefault(); // Prevent default form submission


                var date_of_appointment;
                         var reason_for_appointment;
                         date_of_appointment = document.getElementById('date').value;
                         reason_for_appointment = document.getElementById('reason_for_booking').value;
                
                         if(date_of_appointment && reason_for_appointment){
                            alert("you have been successfully scheduled for an appointment for the given date " + date_of_appointment + " please plan to attend.");
                         }
                       else{
                                alert("unable to schedule you for an appointment");
                         }

         });


});

