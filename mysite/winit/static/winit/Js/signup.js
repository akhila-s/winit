
function myFunction() {
	var name = document.signup.fname.value;
	var name1 = document.signup.lname.value;
	var pwd = document.signup.password.value;
	var pwd1 = document.signup.cpassword.value;
	validateall(name,name1,pwd,pwd1)
	validateName(name);
	validateName(name1);
	validatepwd(pwd,pwd1);
}
function validateName(name){
	var name_length = name.length;
	if(name_length == 0) {
		alert("User name cannot be allowed");
		return false;
	}
	else {
		var n = "^[a-zA-Z]+$";
		var regex = new RegExp(n);
		if(regex.test(name)) {
		}
		else {
			alert("invalid name");
		}
	}
}
function validatepwd(pwd1,pwd2) {
	if(pwd1 == pwd2 && pwd1 != null) {
		if(pwd1.length <= 8) {
			alert("invalid password");
		}
		else {			
		}
	}
}