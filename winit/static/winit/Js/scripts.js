function myFunction() {
	var name = document.myform.firstName.value;
	var name1 = document.myform.LastName.value;
	var pwd = document.myform.pword.value;
	var pwd1 = document.myform.pword1.value;
	var ema = document.myform.email.value;
	// validateName(name);
	// validateName(name1);
	// validatepwd(pwd,pwd1);
	validateEmail(ema);
	}
	function validateName(name){
		var name_length = name.length;
		if(name_length == 0 || name_length < 4||name_length >15) {
			alert("User name cannot be allowed");
			return false;
		}
		else {
			var n = "^([a-zA-Z]+)$";
			var regex = new RegExp(n);
			if(regex.test(n)) {
				alert("valid name");
			}
			else {
				alert("invalid name");
			}
		}
	}
	function validatepwd(pwd1,pwd2) {
		if(pwd1 == pwd2 && pwd1 != null && pwd!= null) {
			if(pwd1.length <= 8 && pwd2.length <= 8) {
				alert("valid password");
			}
			else {
				alert("invalid password");
			}
	}
}
	function validateEmail(email) {
		var em = "^[a-zA-Z0-9]+([\.][a-zA-Z0-9]+)?@[a-zA-Z]+[\.][a-zA-Z]+([\.][a-zA-Z]+)?$";
			var regex = new RegExp(em);
			if(regex.test(email)) {
				alert("valid email");
			}
			else {
				alert("invalid email");
			}
		}

