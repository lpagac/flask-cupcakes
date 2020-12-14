"use strict";

let $cupcakesList = $('#cupcakes-list');
let $newCupcakeForm = $('#add-cupcake');


async function listCupcakes() {
  let response = await axios.get('/api/cupcakes');
  console.log(response.data);
  for (let cupcake of response.data.cupcakes) {
    console.log(cupcake);
    $cupcakesList.append(`<li>${cupcake.flavor} ${cupcake["size"]}</li>`);
  }
}

listCupcakes();