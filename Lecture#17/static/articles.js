fetch("/api/articles")
    .then(response => response.json())
    .then(function (response) {
        var menu = document.getElementById("list-articles");
        var articles = document.getElementById("articles");

        for (let el of response) {
            var div = document.createElement("div");
            div.classList.add("card");
            div.style.width = "18rem";

            var divCardBody = document.createElement("div");
            divCardBody.classList.add("card-body");

            var h5 = document.createElement("h5");
            h5.classList.add("card-title");
            h5.textContent = el.title;

            var h6 = document.createElement("h6");
            h6.classList.add("card-subtitle", "mb-2", "text-body-secondary");
            h6.textContent = el.created_at;

            var p = document.createElement("p");
            p.classList.add("card-text");
            p.textContent = el.body;

            var a = document.createElement("a");
            a.href = "/article/" + el.id + "/delete";
            a.classList.add("card-link");
            a.textContent = "Delete";

            divCardBody.appendChild(h5);
            divCardBody.appendChild(h6);
            divCardBody.appendChild(p);
            divCardBody.appendChild(a);

            div.appendChild(divCardBody);
            articles.appendChild(div);
        }
    });
