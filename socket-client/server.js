// require('dotenv').config()
const express = require('express')
const app = express()
// const port = process.env.PORT | 6000
const port = 5900
const readline = require('readline')
const socketClient = 'socket-client.py'


app.get('/', async (req, res) => {

    let rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })
        
    rl.question("Tu pregunta >> ", (question) => {
        console.log("Tu pregunta: " + question)
        rl.close()

        const pyshell = require('python-shell').PythonShell
    
        let options = {
            mode: 'text',
            pythonPath: '',
            pythonOptions: ['-u'], // get print results in real-time
            scriptPath: '',
            args: [question]
        }
    
        pyshell.run(socketClient, options, (err, results) => {
            if (err) throw err
            console.log('results: %j', results)
        })
    })

    res.json({msg:'Connected'})
})


app.listen(port, (error, server) => {
    if (error) throw error
    if (server) console.log(`\n\nListening on port ${port} ................................\n`)
})
