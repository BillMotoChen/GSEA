function analysis(){

  alert("Start analysis");
}

function jsonfile(){

  var geneid = document.getElementById("geneid").value;
  url = "http://link.g-language.org/"+geneid+"/format=json";
  window.open(url, '_blank');
}

function detailinfo(){

  var geneid = document.getElementById("geneid").value;
  url = "http://link.g-language.org/"+geneid+"/filter=:essential";
  window.open(url, '_blank');



}
