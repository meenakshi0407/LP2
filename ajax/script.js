let btn=document.getElementById("Register");
btn.addEventListener("click",buttonclicked);

let name=document.getElementById("name").value;
let email=document.getElementById("email").value;
let password=document.getElementById("password").value;


function buttonclicked(){
    console.log("Button clicked");
    //get the values from the form
   

    //instantiate the object
    const xhr=new XMLHttpRequest();

    //open the object
    xhr.open("POST","https://dummy.restapiexample.com/api/v1/create",true);
    xhr.setRequestHeader("Content-Type","application/json")

    //onprogress
    onprogress=function(){
        console.log("onprogress..");
    }
    //onload
    xhr.onload=function(){
        if(this.status==200){
        console.log(this.responseText);
        console.log("registered successfully");
        // Save to localStorage
        //localStorage.setItem("registeredUser", JSON.stringify(response));
        }
        else{
            console.log("Created User: "+this.status);
        }
    }
    let params=`name=${name}&email=${email}&password=${password}`;
    //send the request
    xhr.send(params);
    console.log("Request sent");

}