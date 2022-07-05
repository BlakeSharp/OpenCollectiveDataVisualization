document.getElementById('inst').addEventListener("click", event => {
    console.log("hello world")
    document.getElementById('infotext').innerHTML = `<ul style="text-align:left;"><li>Find the community you want the stats for</li><li>Copy the community link and paste it into the input feild</li><li>click 'Get Data'</li></ul>`;
});
document.getElementById('about').addEventListener("click", event => {
    document.getElementById('infotext').innerHTML = "<span>Open Collective Data Visualization is a tool for community leaders and supporters. It supports Open Collective's vision of more transparent crowd-funded projects by making the data provided easier to understand. While Open Collective provides lists of names and amounts, it does little to nothing in terms of visually showing you how it all correlates. That blind spot is what this project fills by providing useful charts, names, and tracking for all parties involved </span>";
});
document.getElementById('tips').addEventListener("click", event => {
    document.getElementById('infotext').innerHTML = "These are some tips for interpreting the graphs"
    document.getElementById('tips').style = ''
});