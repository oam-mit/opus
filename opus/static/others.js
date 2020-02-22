function change()
{
    var ele = document.getElementById('change');
    var files = document.getElementById("id_image")
    ele.innerHTML="Chosen files: "+files.files.item(0).name;
    ele.style.color="red";
}


if (document.title.startsWith("Profile"))
{
    document.getElementById("leaderboard").style.display="none";
    document.getElementById("profile").style.display="none";
    var x=document.getElementById("index");
    x.innerHTML="GAME";
    x.href="/game"

}