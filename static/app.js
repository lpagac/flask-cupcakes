"use strict";

let $cupcakesList = $('#cupcakes-list');
let $newCupcakeForm = $('#add-cupcake');


async function listCupcakes() {
  $cupcakesList.empty();
  let response = await axios.get('/api/cupcakes');


  for (let cupcake of response.data.cupcakes) {
    let $tableRow = $('<tr>');
    $tableRow
      .append(`<td id="img"><img width="100" src="${cupcake.image}"></td>`);
    $tableRow
      .append(`<td>${cupcake.flavor}</td>`);
    $tableRow
      .append(`<td>${cupcake.size}</td>`);
    $tableRow
      .append(`<td>${cupcake.rating}</td>`);
    $cupcakesList.append($tableRow);
  }
}

async function addCupcake() {
  let cupcakeData = {
    flavor: $('#flavor').val(),
    size: $('#size').val(),
    rating: $('#rating').val(),
    image: $('#imgUrl').val(),
  };

  await axios.post('/api/cupcakes', cupcakeData);
  
  $newCupcakeForm.trigger('reset');
}

async function handleAddCupcakeSubmit(e) {
  e.preventDefault();
  
  await addCupcake();
  await listCupcakes();
}


$newCupcakeForm.on("submit", handleAddCupcakeSubmit);
listCupcakes();