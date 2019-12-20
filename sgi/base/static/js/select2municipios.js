$.fn.select2.defaults.set( "theme", "bootstrap" )

processResults = {
    ofMunicipio: function (data) {
        
        let _results = data.map((i) => ({
            id: i.codigo_ibge, 
            text: `${i.nome} (${i.uf})`
        }))

        return {
            results: _results,
            pagination: {
                more: false
            }
        }
    }
}

let sl2Obj = $('select.sgi-select2')

sl2Obj.each((index, obj) => {
    let jqsl2Obj = $(obj)
    let objData = jqsl2Obj.data()      

    jqsl2Obj.select2({
        ajax: {
            url: objData.url,
            dataType: 'json',
            processResults: processResults[objData.processfn] || null
        }
    })
})