export interface Run { t?: string; br?: boolean; sz?: number; b?: boolean; i?: boolean; color?: string }
export interface Para { algn: string; lnSpc: number; spcAft: number; spcBef: number; endSz: number; runs: Run[] }
export interface TextBody { anchor: string; wrap: string; ins: [number, number, number, number]; paras: Para[] }
export interface Shape {
  id: number; name: string; kind: 'sp' | 'pic'; x: number; y: number; w: number; h: number
  rot?: number; flipH?: boolean; flipV?: boolean
  geom?: string; adj?: number; fill?: string | null; line?: { color: string; w: number }
  text?: TextBody; src?: string; alt?: string
}
export interface Step { show: number[]; effect: 'fade' | 'appear' }
export interface Slide { n: number; title: string; bg: string; shapes: Shape[]; steps: Step[]; notes: string }
export interface Deck { lesson: number; width: number; height: number; source: string; slides: Slide[] }
