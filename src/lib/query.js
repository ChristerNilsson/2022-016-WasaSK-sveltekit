import { writable } from 'svelte/store'
function stop () {}
function start (set) {return stop}
export const query = writable("", start)
console.log('store:query loaded')