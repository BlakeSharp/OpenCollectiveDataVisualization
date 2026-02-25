function setActiveButton(activeId) {
    document.querySelectorAll('.headbtn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(activeId).classList.add('active');
}

document.getElementById('inst').addEventListener("click", event => {
    setActiveButton('inst');
    document.getElementById('infotext').innerHTML = `<ul><li>Find the community you want the stats for</li><li>Copy the community link and paste it into the input field</li><li>Click 'View'</li></ul>`;
});

document.getElementById('about').addEventListener("click", event => {
    setActiveButton('about');
    document.getElementById('infotext').innerHTML = "<span>Open Collective Data Visualization is a tool for community leaders and supporters. It supports Open Collective's vision of more transparent crowd-funded projects by making the data provided easier to understand. While Open Collective provides lists of names and amounts, it does little to nothing in terms of visually showing you how it all correlates. That blind spot is what this project fills by providing useful charts, names, and tracking for all parties involved.</span>";
});

document.getElementById('tips').addEventListener("click", event => {
    setActiveButton('tips');
    document.getElementById('infotext').innerHTML = "<span>These are some tips for interpreting the graphs.</span>";
});