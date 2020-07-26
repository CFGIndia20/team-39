(function ($) {
    'use strict'
    $(function (){
        let your_name_value;
        let your_pass_value;
        let name_value;
        let name_value_form;
        let email_value_form;
        let pass_value_form;
        let re_pass_value_form;
        let role;


        // signin-signup toggler
        $("#activate-signin").on('click', function (e) {
            document.getElementById("signup-section").style.display = "none";
            document.getElementById("signin-section").style.display = "block";
        });

        $("#activate-signup").on('click', function (e) {
            document.getElementById("signin-section").style.display = "none";
            document.getElementById("signup-section").style.display = "block";
        });



        // listers for input text and password for sign in
        document.getElementById("your_name").addEventListener('change', function () {
            your_name_value = document.getElementById("your_name").value;
            console.log(your_name_value);
        });

        document.getElementById("Admin").addEventListener('change', function () {
        
            if(document.getElementById("Admin").value)
            {
                role = "admin";
            }
            console.log(role);
        });

        document.getElementById("Donor").addEventListener('change', function () {
            // console.log();
            if(document.getElementById("Donor").value)
            {
                role = "donor";
            }
            console.log(role);
        });

        document.getElementById("your_pass").addEventListener('change', function () {
            
            your_pass_value = document.getElementById("your_pass").value;
            console.log(your_pass_value);
        });

        $("#signin").on('click', function (e) {
            e.preventDefault();

            if(!your_name_value || !your_pass_value)
            {
                alert("please fill the credentials to log in!");
                return;
            }
            
            fetch("http://127.0.0.1:4003/auth",
            {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method: "POST",
                body: JSON.stringify({
                    username : your_name_value,
                    password : your_pass_value
                })
            }).then(response => {
                response.json().then(jwtData => {
                    // console.log('jwtdata check')

                    if (!jwtData['access_token'])
                    {
                        alert(jwtData['description']);
                        document.getElementById("your_name").value = '';
                        document.getElementById("your_pass").value = '';
                        return;
                    }

                    const authToken = "JWT " + jwtData['access_token']
                    //  console.log(authToken);
                    fetch("http://127.0.0.1:4003/signin",
                    {
                        headers: {
                            'Authorization': authToken,
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                        },
                        method: "POST",
                        body: JSON.stringify({
                            name_value: your_name_value,
                            pass_value: your_pass_value
                        })
                    }).then(response => {
                        // console.log(response.json())
                        response.json().then(server_data=>{
                            // console.log(server_data)
                            // console.log("comment out line 85,86 & during integration, uncomment path code below this & add html file path to redirect");
                            if(role == "donor")
                            {
                                window.location.replace("../donor-report/index.html");
                            }
                            else{
                                window.location.replace("./index.html");
                            }
                             //location path should be relative wrt index.html file
                        });
                    });
                })
            });

            // fetch("http://127.0.0.1:5000/signin",
            //         {
            //             headers: {
            //                 // 'Authorization': authToken,
            //                 'Accept': 'application/json',
            //                 'Content-Type': 'application/json'
            //             },
            //             method: "POST",
            //             body: JSON.stringify({
            //                 name_value: your_name_value,
            //                 pass_value: your_pass_value
            //             })
            //         }).then(response => {
            //             // console.log(response.json())
            //             response.json().then(server_data=>{
            //                 console.log(server_data)
            //                 console.log("comment out line 85,86 & during integration, uncomment path code below this & add html file path to redirect");
            //                 // window.location.replace("./index.html"); //location path should be relative wrt index.html file
            //             });
            //         });
            
        });
        

        // listers for input text and password for sign up
        document.getElementById("name").addEventListener('change', function () {
            name_value_form = document.getElementById("name").value;
        });

        document.getElementById("email").addEventListener('change', function () {
            email_value_form = document.getElementById("email").value;
        });

        document.getElementById("pass").addEventListener('change', function () {
            pass_value_form = document.getElementById("pass").value;
        });

        document.getElementById("re_pass").addEventListener('change', function () {
            re_pass_value_form = document.getElementById("re_pass").value;
            if(pass_value_form !== re_pass_value_form)
            {
                alert("passwords don't match!!");
                document.getElementById("pass").value = "";
                document.getElementById("re_pass").value = "";
            }
                
        });

        $("#signup").on('click', function (e) {
            e.preventDefault();

            if(!pass_value_form || !re_pass_value_form || !email_value_form || !name_value_form)
            {
                alert("please complete the form to register!!");
                return;
            }
            
            
            fetch("http://127.0.0.1:4003/signup",
                {
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    method: "POST",
                    body: JSON.stringify({
                        name_value: name_value_form,
                        email_value: email_value_form,
                        pass_value:pass_value_form,
                        re_pass_value:re_pass_value_form
                    })
                }).then(response => {
                    response.json().then(server_data=>{
                       if(server_data['message'])
                       {
                           alert(server_data['message'])
                           return;
                       }
                       alert('user successfully created, login using createrd user!');
                       window.location.replace("./index.html");
                    });
                });
         });


        
    });

})(jQuery);