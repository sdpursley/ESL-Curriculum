import type { Deck } from './types'
/** Lessons that have a presenter deck. Each deck JSON is loaded on demand as its own chunk. */
export const DECK_LESSONS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
const loaders: Record<number, () => Promise<{ default: unknown }>> = {
  1: () => import('../decks/lesson1.json'),
  2: () => import('../decks/lesson2.json'),
  3: () => import('../decks/lesson3.json'),
  4: () => import('../decks/lesson4.json'),
  5: () => import('../decks/lesson5.json'),
  6: () => import('../decks/lesson6.json'),
  7: () => import('../decks/lesson7.json'),
  8: () => import('../decks/lesson8.json'),
  9: () => import('../decks/lesson9.json'),
  10: () => import('../decks/lesson10.json'),
  11: () => import('../decks/lesson11.json'),
  12: () => import('../decks/lesson12.json'),
  13: () => import('../decks/lesson13.json'),
}
export const hasDeck = (n: number) => n in loaders
export const loadDeck = async (n: number) => (await loaders[n]()).default as Deck
