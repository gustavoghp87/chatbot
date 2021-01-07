const app = require('express')()
let readline = require('readline')


const port = process.env.PORT || 4005

app.get('/', async (req, res) => {

    let rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })
        
    rl.question(">> ", (answer) => {
        console.log("Hello " + answer)
        rl.close()

        const pyshell = require('python-shell').PythonShell
    
        let options = {
            mode: 'text',
            pythonPath: '',
            pythonOptions: ['-u'], // get print results in real-time
            scriptPath: '',
            args: [answer, 'obama']
        }
    
        pyshell.run('main.py', options, (err, results) => {
            if (err) throw err
            console.log('results: %j', results)
        })
    })


    res.json({msg:'All right'})
})

const server = app.listen(port)
if (server) console.log(`\n\nListening on port ${port} ................................\n`)
