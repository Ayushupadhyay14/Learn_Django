// Define the base url:

const API_URL = "/api/product/";
const productList = document.getElementById("product-list");
async function fetchProducts() {
  const response = await fetch(API_URL);
  if (response.ok) {
    const products = await response.json();
    productList.innerHTML = products.map((product) => (
      <tr>
        <td>${product.id}</td>
        <td>${product.name}</td>
        <td>₹${product.price}</td>
        <td></td>
      </tr>
    ));
  }
}
fetchProducts();

// document.addEventListener("DOMContentLoaded", function () {
//   fetch("/api/product/")
//     .then((response) => response.json())
//     .then((products) => {
//       const tbody = document.getElementById("product-table-body");
//       tbody.innerHTML = ""; // clear existing rows

//       if (products.length === 0) {
//         tbody.innerHTML =
//           '<tr><td colspan="4" class="text-center">No products available.</td></tr>';
//       } else {
//         products.forEach((product) => {
//           const row = document.createElement("tr");

//           row.innerHTML = `
//             <td>${product.id}</td>
//             <td>${product.name}</td>
//             <td>₹${product.price}</td>
//             <td>
//               <a href="/edit/${product.id}/" class="btn btn-sm btn-warning">Edit</a>
//               <a href="/delete/${product.id}/" class="btn btn-sm btn-danger">Delete</a>
//             </td>
//           `;

//           tbody.appendChild(row);
//         });
//       }
//     })
//     .catch((error) => console.error("Error loading products:", error));
// });
// fetch();
