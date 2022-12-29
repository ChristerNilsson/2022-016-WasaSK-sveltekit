import { writable } from 'svelte/store'

function stop () {}
function start (set) {return stop}

export const query = writable("", start)
export const innerwidth = writable(1000, start)
export const multiselect = writable('nix nix nix nix nix nix nix nix'.split(' '),start)

console.log('store:writable loaded')