const puppeteer = require('puppeteer');
// const proxy = "192.168.125.11:7000";
const proxy = "192.168.1.2:7000"; // your eth interface here

(async () => {
	const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
	try {
		const page = await browser.newPage();

		// Make sure we handle any popup windows
		page.on('dialog', async dialog => {
			console.log(dialog.message());
			await dialog.dismiss();
		});
		await page.goto('http://' + proxy + '/', {
			waitUntil: 'networkidle0',
		});
		var content = await page.content();
		console.log(content);
	}
	catch (err) {
		console.error(err.message);
	}
	finally {
		await browser.close();
	}
})();
