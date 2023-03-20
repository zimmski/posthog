export function HogLogo({ style }: React.PropsWithoutRef<JSX.IntrinsicElements['svg']>): JSX.Element {
    return (
        // eslint-disable-next-line react/forbid-dom-props
        <svg width="58" height="34" viewBox="0 0 58 34" fill="none" xmlns="http://www.w3.org/2000/svg" style={style}>
            <path
                d="M0 23.8578L9.55594 33.4009H0V23.8578ZM0 21.472L11.9449 33.4009H21.5009L0 11.9289V21.472ZM0 9.54311L23.8898 33.4009H33.4458L0 0V9.54311ZM11.9449 9.54311L35.8348 33.4009V23.8578L11.9449 0V9.54311ZM23.8898 0V9.54311L35.8348 21.472V11.9289L23.8898 0Z"
                fill="#F9BD2B"
            />
            <path
                d="M57.3356 29.5836C54.8874 29.5836 52.5405 28.6122 50.8108 26.8849L37.5243 13.6161V33.4009H57.3356V29.5836Z"
                fill="black"
            />
            <path
                d="M43.2578 29.5836C44.3133 29.5836 45.169 28.7291 45.169 27.675C45.169 26.6209 44.3133 25.7664 43.2578 25.7664C42.2023 25.7664 41.3466 26.6209 41.3466 27.675C41.3466 28.7291 42.2023 29.5836 43.2578 29.5836Z"
                fill="white"
            />
            <path d="M0 33.4009H9.55594L0 23.8578V33.4009Z" fill="#1D4AFF" />
            <path d="M11.9449 11.9289L0 0V9.54311L11.9449 21.472V11.9289Z" fill="#1D4AFF" />
            <path d="M0 11.9289V21.472L11.9449 33.4009V23.8578L0 11.9289Z" fill="#1D4AFF" />
            <path d="M23.8898 11.9289L11.9449 0V9.54311L23.8898 21.472V11.9289Z" fill="#F54E00" />
            <path d="M11.9449 33.4009H21.5008L11.9449 23.8578V33.4009Z" fill="#F54E00" />
            <path d="M11.9449 11.9289V21.472L23.8898 33.4009V23.8578L11.9449 11.9289Z" fill="#F54E00" />
        </svg>
    )
}
