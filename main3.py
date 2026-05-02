from pyscript import document

activities = [
    {
        "image": "intrams.jpg",
        "title": "Intrams",
        "desc": "Students participating in intramural sports activities"
    },
    {
        "image": "Snack Time.jpg",
        "title": "Snack Time",
        "desc": "Students enjoying break time"
    },
    {
        "image": "C.A.T Graduation.jpg",
        "title": "C.A.T Graduation Day",
        "desc": "Students graduating from the C.A.T program"
    }
]

gallery = document.getElementById("gallery")

for item in activities:

    card = document.createElement("div")
    card.className = "photo"

    img = document.createElement("img")
    img.src = item["image"]

    title = document.createElement("h4")
    title.innerText = item["title"]

    desc = document.createElement("p")
    desc.innerText = item["desc"]

    card.appendChild(img)
    card.appendChild(title)
    card.appendChild(desc)

    gallery.appendChild(card)