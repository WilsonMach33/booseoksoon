song = [["SONG1", "ALBUM"], ["SONG2", "ALBUM"], ["SONG3", "ALBUM"], ["SONG4", "ALBUM"]]

const cardTemplate = document.querySelector("[card-template]")



data => {
    data.forEach(song => {
        const card = cardTemplate.content.cloneNode(true).children[0]
        const header = card.querySelector("[card-header]")
        const body = card.querySelector("[card-body]")
        header.textContent = data[0]
        header.textContent = data[1]
        
    })
    
}