let mysql = require('mysql2')
let crypto = require('crypto');

class Database {

    constructor() {
        this.connection = mysql.createConnection({
            host: '127.0.0.1',
            user: 'user',
            password: 'M@k3l@R!d3s$',
            database: 'cybercore'
        });
    }

    async connect() {
        return new Promise((resolve, reject) => {
            this.connection.connect((err) => {
                if (err)
                    reject(err)
                resolve()
            });
        })
    }

    async getKeyStore() {
        return new Promise(async (resolve, reject) => {
            let stmt = 'SELECT * FROM keystore';
            this.connection.query(stmt, (err, result) => {
                if (err)
                    reject(err)
                resolve(result)
            })
        });
    }

    async login(username, password) {
        return new Promise((resolve, reject) => {
            let stmt = 'SELECT username, password from users WHERE username = ?';

            this.connection.query(stmt, [username], (err, result) => {
                if (err)
                    reject(err)

                if (typeof result !== 'undefined' && result.length > 0) {
                    let password_hash = crypto.createHash('md5').update(password).digest('hex');

                    if (result[0].password == password_hash) {
                        resolve(result[0]);
                    }
                }

                reject(new Error('Invalid Credentials!'));
            })
        })
    }

    async check_user(username) {
        return new Promise((resolve, reject) => {
            let stmt = `SELECT username from users WHERE username='${username}'`;

            this.connection.query(stmt, (err, result) => {
                if (err)
                    reject(err);


                if (typeof result !== 'undefined' && result.length > 0)
                    resolve(result[0].username);

                reject(new Error('Invalid Credentials!'));
            });

        });
    }
}

module.exports = Database;