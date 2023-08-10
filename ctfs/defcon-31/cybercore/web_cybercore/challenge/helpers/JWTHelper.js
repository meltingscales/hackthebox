const jwt    = require('jsonwebtoken');
db.getKeyStore().then(keyStore => global.keyStore = keyStore);

module.exports = {
	sign(data, kid='2') {
		return new Promise(async (resolve, reject) => {
			try {
                keyData = keyStore.filter(i => i.kid == kid)
                if(keyData.length === 0) reject();
                resolve(jwt.sign(data, keyData[0].secret, {
			        algorithm: 'HS256',
			        header: { kid: kid }
		        }));
            } catch (e) {
				reject(e);
			}
        });
	},
	async verify(token, kid) {
		return new Promise(async (resolve, reject) => {
			try {
                keyData = keyStore.filter(i => i.kid == kid)

                if(keyData.length === 0) reject();
				return resolve(jwt.verify(token, keyData[0].secret, { algorithm: 'HS256' }));
			} catch (e) {
				reject(e);
			}
		});
	}
};