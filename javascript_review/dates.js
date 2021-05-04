// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
const getDayName = (dateString) => {
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    let dayName;
    const date = new Date(dateString);
    dayName = days[date.getDay()];
    return dayName;
}

console.log(getDayName('10/11/2009'));