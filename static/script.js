// JavaScript to set today's date as the value of the input field
const today = new Date();
const year = today.getFullYear();
const month = ("0" + (today.getMonth() + 1)).slice(-2); // Add leading zero if needed
const day = ("0" + today.getDate()).slice(-2); // Add leading zero if needed

const formattedDate = `${year}-${month}-${day}`; // Format the date as YYYY-MM-DD

document.getElementById("start_date").value = formattedDate; // Set today's date as the input value

let buttonclicked=false;
let graphclicked=0;
function handlebut(){
    if(buttonclicked){
        location.reload();
    }
    else{
        buttonclicked=true;
        document.getElementById("button1").innerHTML="Reset";
        myfun();
    }
}
function handlegraph(){
    graphclicked=1;
    myfun1();
}
function myfun1() {
    document.getElementById("button1").value
    const curr_pres = document.getElementById("curr_pres").value;
    const curr_total = document.getElementById("curr_total").value;
    let start_date = document.getElementById("start_date").value;
    fetch(`/run-python?curr_pres=${curr_pres}&curr_total=${curr_total}&start_date=${start_date}&graphclicked=${graphclicked}`)
    //fetch('/run-python')  
    // // Request to the Python backend
        .then(response => response.json())  // Parse JSON response <img src="${data.plot_url}" alt="Attendance Plot" style="width: 100%; height: auto;">
        .then(data => {
            document.getElementById("res").innerHTML = `
                <p>Current Attendance: ${data.curr_attandance.toFixed(2)}%</p>
                <p>If daily present Attendance at end: ${data.attendance_percentage.toFixed(2)}%</p>
                <p>After Absence: ${data.attendance_after_absent.toFixed(2)}%</p>
                <p>Leaves Left: ${data.leaves_left_hr.toFixed(2)} hours or ${data.leaves_left_day.toFixed(2)} days for above 75%</p>
                
            `;
        })
        .catch(error => console.error('Error:', error));
}

function myfun() {
    document.getElementById("button1").value
    const curr_pres = document.getElementById("curr_pres").value;
    const curr_total = document.getElementById("curr_total").value;
    let start_date = document.getElementById("start_date").value;
    fetch(`/run-python?curr_pres=${curr_pres}&curr_total=${curr_total}&start_date=${start_date}&graphclicked=${graphclicked}`)
    //fetch('/run-python')  
    // // Request to the Python backend
        .then(response => response.json())  // Parse JSON response <img src="${data.plot_url}" alt="Attendance Plot" style="width: 100%; height: auto;">
        .then(data => {
            document.getElementById("res").innerHTML = `
                <p>Current Attendance: ${data.curr_attandance.toFixed(2)}%</p>
                <p>If daily present Attendance at end: ${data.attendance_percentage.toFixed(2)}%</p>
                <p>After Absence: ${data.attendance_after_absent.toFixed(2)}%</p>
                <p>Leaves Left: ${data.leaves_left_hr.toFixed(2)} hours or ${data.leaves_left_day.toFixed(2)} days for above 75%</p>
                
            `;
        })
        .catch(error => console.error('Error:', error));
}
