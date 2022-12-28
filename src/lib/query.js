import { writable } from 'svelte/store'

function stop () {}
function start (set) {return stop}

export const query = writable("", start)
export const innerwidth = writable(1000, start)

console.log('store:writable loaded')