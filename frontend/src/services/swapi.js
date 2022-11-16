export async function getPesonagens(page = 1){
    const response = await fetch("https://swapi.py4e.com/api/people/?page=" + page);
    const person = await response.json();
    return person
}

export async function getNaves(page = 1){
    const response = await fetch("https://swapi.py4e.com/api/starships/?page=" + page);
    const person = await response.json();
    return person
}

export async function getVeiculos(page = 1){
    const response = await fetch("https://swapi.py4e.com/api/vehicles/?page=" + page);
    const person = await response.json();
    return person
}

export async function getPlanetas(page = 1){
    const response = await fetch("https://swapi.py4e.com/api/planets/?page=" + page);
    const person = await response.json();
    return person
}

export async function getUsuarios(page = 1){
    const response = await fetch("http://localhost:3000/users?page=" + page);
    const person = await response.json();
    return person
}

