function send(){
let c=document.getElementById("chat")
let m=document.getElementById("msg")
c.innerHTML+="<p>You: "+m.value+"</p><p>AI: I will guide your career.</p>"
m.value=""
}
