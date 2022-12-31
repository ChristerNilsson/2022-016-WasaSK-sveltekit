import _ from 'lodash'

export const range = _.range
export const log = console.log

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

export function spaceShip (a,b) {
	if (a < b) return -1
	else if (a == b) return 0
	return 1 
}

export function multiSort (a,b,indexes) {
	for (const i in range(indexes.length)) {
		const index = Math.abs(indexes[i])-1 // 0..
		let res = spaceShip(a[index],b[index])
		if (res != 0) return indexes[i] < 0 ? -res : res
	}
}
