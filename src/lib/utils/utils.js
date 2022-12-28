const arr = []
const DAY = 86400*1000 // ms
arr.push([365*DAY, " år"])
arr.push([30*DAY," månader"])
arr.push([7*DAY," veckor"])
arr.push([DAY," dagar"])
arr.push([3600*1000," timmar"])
arr.push([60*1000," minuter"])
arr.push([1000," sekunder"])
arr.push([1," millisekunder"])

export const timeSince = (date1) => {
	date1 = new Date(date1)
	const date2 = new Date()
	const ms = Math.floor(date2 - date1)
	if (ms < 0) return ""
	for (const [count,text] of arr) {
		let interval = Math.floor(ms / count)
		if (interval > 1) return interval + text
	}
}

// export const timeSince = (date1) => {
// 	const DAY = 86400 // seconds
// 	date1 = new Date(date1)
// 	const date2 = new Date()
// 	const seconds = Math.floor((date2 - date1) / 1000)
// 	let interval = Math.floor(seconds / (365*DAY))
// 	if (interval > 1) return interval + " år"
// 	interval = Math.floor(seconds / (30*DAY))
// 	if (interval > 1) return interval + " månader"
// 	interval = Math.floor(seconds / (7*DAY))
// 	if (interval > 1) return interval + " veckor"
// 	interval = Math.floor(seconds / DAY)
// 	if (interval > 1) return interval + " dagar"
// 	interval = Math.floor(seconds / 3600)
// 	if (interval > 1) return interval + " timmar"
// 	interval = Math.floor(seconds / 60)
// 	if (interval > 1) return interval + " minuter"
// 	return Math.floor(seconds) + " sekunder"
// }
