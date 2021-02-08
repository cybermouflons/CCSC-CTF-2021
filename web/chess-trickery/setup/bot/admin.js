const puppeteer = require('puppeteer');
// CHANGE THE FOLLOWING TO THE HOST'S IP ADDRESS
// const proxy = "192.168.125.11"; // Hosts IP address - required for this to work
const proxy = "172.16.3.11"; // Docker Proxy IP address

(async () => {
	const browser = await puppeteer.launch({args: ['--no-sandbox', '--disable-setuid-sandbox']});
	try {
		const page = await browser.newPage();

		// Make sure we handle any popup windows
		page.on('dialog', async dialog => {
			console.log(dialog.message());
			await dialog.dismiss();
		});
		await page.goto('http://' + proxy + '/login.php');
		await page.type('#username', 'admin');
		await page.type('#password', "uYhQUkw=U}j}AX/N(FQJ ,k}?5!k^S\\ Iy6");
		await page.click('.btn-primary');
		await page.waitForSelector('.voila');
		const cookies = await page.cookies();
		// console.log(cookies);

		// 2nd request
		await page.setCookie(...cookies);
		await page.goto('http://' + proxy + '/6d81e248c410d40a60a386d79fa97aa6595f58e846f91611b705cc8995e860cd.php');

		var content = await page.content();

		innerText = await page.evaluate(() =>  {
			return JSON.parse(document.querySelector("body").innerText);
		});

		console.log(innerText.link);

		// 3rd request
		/* 		await page.setCookie(...cookies); */
		const url = innerText.link;
		let domain = (new URL(url));
		domain = domain.hostname;
		console.log(domain);

		if (domain === proxy) {
			await page.goto(innerText.link);
			var content = await page.content();
			console.log(content);
		}
		else {
			console.log("Domain not valid, probably external");
		}
	}
	catch (err) {
		console.error(err.message);
	}
	finally {
		await browser.close();
	}
})();
