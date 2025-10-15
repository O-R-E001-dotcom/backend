function Footer() {
    const year = new Date().getFullYear();

    return (
        <footer className="footer">
            <p>© {year} My App</p>
        </footer>
    );
}

export default Footer;