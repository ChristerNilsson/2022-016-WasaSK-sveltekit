import { writable } from 'svelte/store'

function stop () {}
function start (set) {return stop}

export const query = writable("", start)
export const innerwidth = writable(1000, start)

export const a = writable('nix',start) // ålder
export const b = writable('nix',start) // typ
export const c = writable('nix',start) // lag
export const d = writable('nix',start) // nivå
export const e = writable('nix',start) // tid
export const f = writable('nix',start) // kön
export const g = writable('nix',start) // år

console.log('store:writable loaded')