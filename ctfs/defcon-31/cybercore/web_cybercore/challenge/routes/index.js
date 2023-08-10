const express = require('express');
const router = express.Router();
const JWTHelper = require('../helpers/JWTHelper');
const fs = require('fs');
const AuthMiddleware = require('../middleware/AuthMiddleware');

const response = data => ({ message: data });

router.get('/', async (req, res) => {
	return res.render('index.html')
});

router.post('/', async (req, res) => {
	const { username, password } = req.body;

	if (username && password) {
		return db.check_user(username).then((user) => {
			db.login(user, password)
				.then(async () => {
					let token = await JWTHelper.sign({
						username
					});

					res.cookie('session', token, { maxAge: 259200000 });
					return res.send(response('User authenticated successfully!'));
				}).catch((e) => res.status(403).send(response('Invalid username or password!')));

		}).catch((e) => res.status(403).send(response('Invalid username or password!')));
	}

	return res.status(500).send(response('Missing parameters!'));
});

router.get('/home', AuthMiddleware, async (req, res) => {
	flag = fs.readFileSync('/flag.txt', 'utf-8');
	return res.render('home.html', { flag: flag });
});


router.get('/logout', (req, res) => {
	res.clearCookie('session');
	return res.redirect('/');
});

module.exports = () => {
	return router;
};