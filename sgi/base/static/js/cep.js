class CEPService {

    static async consulta(cep) {
        let url = `/base/geo/endereco/cep/${cep}`
        let req = new Request(url, { method: 'GET' })
        try {
            let resp = await fetch(req);
            return await resp.json();
        } catch (err) {
            console.error(err);
        }
    }
}

document.getElementById('id_cep').addEventListener('change', async (event) => {
    let cep = event.target.value
    let result = await CEPService.consulta(cep)

    Object.entries(result).forEach(([k, v]) => {

        if (k === 'localidade') 
            k = 'cidade'

        const el = document.getElementById(`id_${k}`)
        
        if (el)
            el.value = v
    });
})
