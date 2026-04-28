function loginUser() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;

    // Demo credentials
    if (user === "tenant" && pass === "rent123") {
        alert("Login successful");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid username or password");
    }
    return false;
}
