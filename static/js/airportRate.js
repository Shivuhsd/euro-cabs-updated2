let result;
const baseUrl = 'http://127.0.0.1:8000'

console.log(baseUrl)

const getDest = async()=> {

    document.getElementById('price').style.display = 'none';

    const fromCity = document.getElementById('from')

    const where = document.getElementById('where')

    const destUrl = `${baseUrl}/users/airportDest?dest=${fromCity.value}`;

    console.log(destUrl)

    const response = await fetch(destUrl)
    result = await response.json()

    where.innerHTML = ''
    console.log('Hellow')
    console.log(result)

    const op = document.createElement('option')
        op.value = 'none'
        op.innerText = 'Select A City'

        where.appendChild(op)

    for(let i of result.dest)
    {
        const op = document.createElement('option')
        op.value = i.id
        op.innerText = i.to

        where.appendChild(op)
    }

}


const getPrice = async() => {
    const where = document.getElementById('where').value;

    for(let i of result.dest )
    {
        if(i.id === where)
        {
            document.getElementById('price').style.display = 'flex';
            document.getElementById('price').style.justifyContent = 'space-between'
            document.getElementById('night').value = i.nightRate;
            document.getElementById('day').value = i.dayRate
        }
        
    }
}