 $("#searching_form").submit(function(e){


        e.preventDefault();
        var reg_number=document.getElementById("reg").value;

        var csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value;

        $.ajax({

          type:"POST",
          headers: { "X-CSRFToken": csrf },
          url:"/profile/search/",
          data:{
            'reg':reg_number

          },

          beforeSend:function(){
            document.getElementById("form_spinner").classList.remove("d-none");
            document.getElementById("form_status_text").innerHTML="Processing";

          },

          success:function(response){
            if(response!="No Data Found"){
            document.getElementById("result_search").innerHTML=" ";
             $('#result_search').append(response);
             document.getElementById("form_spinner").classList.add("d-none");
             document.getElementById("form_status_text").innerHTML="Submit";
              
            
            }

          },

        
        
        });

      });

  
