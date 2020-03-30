$("#aptitude_form").submit(function(e){

    e.preventDefault();
    var csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value;
    var answer=document.getElementById("id_answer").value;

    $.ajax({
        type:"POST",
        url:"/game/check_aptitude",
        headers: { "X-CSRFToken": csrf },
        data:{
            'ans':answer

          },

          beforeSend:function(){
            const Toast = Swal.mixin({
              toast: true,
              position: 'top',
              showConfirmButton: false,
              timer: 3000,
              timerProgressBar: true,
              onOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
              }
            })
            
            Toast.fire({
              icon: 'question',
              title: 'Checking'
            })

          },

          success:function(response){
            if(response!="correct"){
              Swal.fire({
                title: 'Incorrect Response!!',
                width: 600,
                padding: '3em',
                //background: "rgba(26, 21, 15, 0.39)",
                backdrop: `
                  rgba(0,0,123,0.4)
                `,
                icon:'error',
               
              });
            
            }

            else if (response=="correct"){
              Swal.fire({
                title: 'Correct Answer!!',
                width: 600,
                padding: '3em',
                //background: "rgba(26, 21, 15, 0.39)",
                backdrop: `
                  rgba(0,0,123,0.4)
                `,
                icon:'success',
                onClose: () =>{document.location.reload();}
              });

                
            }

           


          },
    });


});
