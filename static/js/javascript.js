const charField = document.querySelector("searchFiels");
const tableOutput = docment.querySelector(".table-output");
const apptable = docment.querySelector(".app-table");
const paginationcontainer = document.querySelector(".pagination-container");
tableOutput.style.display = "none";
noResult = docment.querySelector(".no-result");
const tbody = docment.querySelector(".table-body");

searchField.addEventListener("keyup",(e)=>{
const searchValue = e.target.value;
if (searchValue.trim().length > 0){
    paginationContainer.style.display = "none";
    tbody.innerHTML ="";
    fetch("/livre/search-ajax", {
    body: JSON.stringify({searchText:searchValue}),
    method : "POST",
    })
    .then((res) => res.json())
    .then((data)=> {
    console.log("data, data");
    appTable.style.display = "none";
    tableOutput.style.display = "block";

    if (data.length ===0){
        noResult.style.display = "none";
    }else{
        noResult.style.display = "none";
        dara.forEach((item)=>{
        tbody.innerHTML+=
        <tr>
        <td>${item.titre}</td>
        <td>${item.auteur}</td>
        <td>${item.description}</td>
        </tr>
        });
    }
});
}else{
    tableOuput.style.display = "none";
    appTable.style.display = "block";
}
});
