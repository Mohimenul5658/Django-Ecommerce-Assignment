document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("productSearch");
    const productCards = document.querySelectorAll(".product-card");

    if (!searchInput) {
        return;
    }

    searchInput.addEventListener("input", function () {

        const searchText = searchInput.value.toLowerCase().trim();

        productCards.forEach(function (card) {

            const productNameElement =
                card.querySelector(".product-name");

            const productCategoryElement =
                card.querySelector(".product-category");

            if (!productNameElement || !productCategoryElement) {
                return;
            }

            const productName =
                productNameElement.textContent.toLowerCase();

            const productCategory =
                productCategoryElement.textContent.toLowerCase();

            const isMatch =
                productName.includes(searchText) ||
                productCategory.includes(searchText);

            card.style.display = isMatch ? "" : "none";

        });

    });

});