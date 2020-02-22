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
            $("#result_search").append('Processing...');

          },

          success:function(response){
            if(response!="No Data Found"){
              document.getElementById("result_search").innerHTML=" ";
              $('#result_search').append(response);
            
            }

          },

        
        
        });

      });

  
