// Site settings.
// Teacher slides: set a lesson to true once public/downloads/slides/Lesson<N>_Slides.pptx exists.
// Lessons set to false show "coming soon".
export const SLIDES_READY: Record<number, boolean> = { 1: true, 2: true, 3: true, 4: true, 5: true, 6: true, 7: true, 8: true, 9: true, 10: true, 11: true, 12: true, 13: true }
export const SLIDES_AVAILABLE = (n: number) => SLIDES_READY[n] === true
export const slidePath = (n: number) => `downloads/slides/Lesson${n}_Slides.pptx`
/** In-browser presenter route (HashRouter), opened in a new tab. */
export const presentHref = (n: number) => `#/present/${n}`
export const LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-sa/4.0/'
export const DISCLAIMER = 'Provided as-is for educational use, without warranty of any kind.'
/** Teacher exam files in public/downloads/exams/. */
export const examPath = (f: string) => `downloads/exams/${f}`

/** Level 1 presenter route (HashRouter), opened in a new tab. Level 1 file paths come from src/content_level1.json. */
export const level1PresentHref = (n: number) => `#/level1/present/${n}`
/** Level 3 presenter route; Level 3 file paths come from src/content_level3.json. */
export const level3PresentHref = (n: number) => `#/level3/present/${n}`
