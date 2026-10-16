import raw from './content.json'
import sizesRaw from './sizes.json'
export interface Word { img: string; word: string; star: boolean }
export interface Lesson { n: number; title: string; grammar: string; week: number; words: Word[]; audio: string;
  listening: string; grammarHtml: string; homework: string; teacher: string }
export interface Content { semester: string; routine: string; teacherGuide: string; studentHowTo: string;
  lessons: Lesson[]; credit: string; creditHtml: string; downloads: { pdf: string; docx: string } }
export const content = raw as Content
export const sizes = sizesRaw as Record<string, number>
export const mb = (b: number) => b < 1048576 ? `${Math.max(1, Math.round(b / 1024))} KB` : `${(b / 1048576).toFixed(1)} MB`
