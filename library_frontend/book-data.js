// Sample book data for the application
const sampleBooks = [
    {
        id: 1,
        title: 'Atomic Habits',
        author: 'James Clear',
        isbn: '978-0735211292',
        publisher: 'Penguin',
        year: 2018,
        pages: 320,
        category: 'Self-Help',
        language: 'English',
        location: 'A-23-5',
        callNumber: '158.1 CLE',
        copies: 5,
        available: 5,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1763768861268-cb6b54173dbf?w=400',
        description: 'No matter your goals, Atomic Habits offers a proven framework for improving—every day. James Clear, one of the world\'s leading experts on habit formation, reveals practical strategies that will teach you exactly how to form good habits, break bad ones, and master the tiny behaviors that lead to remarkable results.',
        tags: ['Habits', 'Self-Improvement', 'Productivity', 'Psychology']
    },
    {
        id: 2,
        title: 'Deep Work',
        author: 'Cal Newport',
        isbn: '978-1455586691',
        publisher: 'Grand Central Publishing',
        year: 2016,
        pages: 296,
        category: 'Business',
        language: 'English',
        location: 'B-15-8',
        callNumber: '650.1 NEW',
        copies: 3,
        available: 2,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1759234008322-70456fcf6aec?w=400',
        description: 'Deep work is the ability to focus without distraction on a cognitively demanding task. It\'s a skill that allows you to quickly master complicated information and produce better results in less time.',
        tags: ['Focus', 'Productivity', 'Work', 'Success']
    },
    {
        id: 3,
        title: 'Thinking, Fast and Slow',
        author: 'Daniel Kahneman',
        isbn: '978-0374533557',
        publisher: 'Farrar, Straus and Giroux',
        year: 2011,
        pages: 499,
        category: 'Science',
        language: 'English',
        location: 'C-08-2',
        callNumber: '153.4 KAH',
        copies: 4,
        available: 3,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1725869973689-425c74f79a48?w=400',
        description: 'A groundbreaking tour of the mind explaining the two systems that drive the way we think and make choices.',
        tags: ['Psychology', 'Decision Making', 'Behavioral Economics', 'Cognitive Science']
    },
    {
        id: 4,
        title: 'The Alchemist',
        author: 'Paulo Coelho',
        isbn: '978-0062315007',
        publisher: 'HarperOne',
        year: 1988,
        pages: 197,
        category: 'Fiction',
        language: 'English',
        location: 'D-12-4',
        callNumber: 'FIC COE',
        copies: 6,
        available: 0,
        status: 'borrowed',
        image: 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400',
        description: 'A classic novel about a young Andalusian shepherd in his journey to the pyramids of Egypt, after having a recurring dream of finding a treasure there.',
        tags: ['Adventure', 'Philosophy', 'Dreams', 'Journey']
    },
    {
        id: 5,
        title: 'Sapiens',
        author: 'Yuval Noah Harari',
        isbn: '978-0062316097',
        publisher: 'Harper',
        year: 2011,
        pages: 443,
        category: 'Non-Fiction',
        language: 'English',
        location: 'E-05-1',
        callNumber: '909 HAR',
        copies: 4,
        available: 4,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1589998059171-988d887df646?w=400',
        description: 'From a renowned historian comes a groundbreaking narrative of humanity\'s creation and evolution that explores the ways in which biology and history have defined us.',
        tags: ['History', 'Anthropology', 'Evolution', 'Humanity']
    },
    {
        id: 6,
        title: '1984',
        author: 'George Orwell',
        isbn: '978-0451524935',
        publisher: 'Signet Classic',
        year: 1949,
        pages: 328,
        category: 'Fiction',
        language: 'English',
        location: 'D-18-7',
        callNumber: 'FIC ORW',
        copies: 5,
        available: 5,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400',
        description: 'A dystopian social science fiction novel and cautionary tale about the dangers of totalitarianism.',
        tags: ['Dystopia', 'Classic', 'Politics', 'Society']
    },
    {
        id: 7,
        title: 'The Lean Startup',
        author: 'Eric Ries',
        isbn: '978-0307887894',
        publisher: 'Crown Business',
        year: 2011,
        pages: 336,
        category: 'Business',
        language: 'English',
        location: 'B-22-3',
        callNumber: '658.11 RIE',
        copies: 3,
        available: 3,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1621944190310-e3cca1564bd7?w=400',
        description: 'How today\'s entrepreneurs use continuous innovation to create radically successful businesses.',
        tags: ['Startup', 'Entrepreneurship', 'Innovation', 'Business Strategy']
    },
    {
        id: 8,
        title: 'Educated',
        author: 'Tara Westover',
        isbn: '978-0399590504',
        publisher: 'Random House',
        year: 2018,
        pages: 334,
        category: 'Non-Fiction',
        language: 'English',
        location: 'E-14-6',
        callNumber: '378.092 WES',
        copies: 4,
        available: 2,
        status: 'reserved',
        image: 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400',
        description: 'A memoir about a young woman who, kept out of school, leaves her survivalist family and goes on to earn a PhD from Cambridge University.',
        tags: ['Memoir', 'Education', 'Family', 'Transformation']
    },
    {
        id: 9,
        title: 'The 7 Habits of Highly Effective People',
        author: 'Stephen R. Covey',
        isbn: '978-1982137274',
        publisher: 'Simon & Schuster',
        year: 1989,
        pages: 464,
        category: 'Self-Help',
        language: 'English',
        location: 'A-28-2',
        callNumber: '158.1 COV',
        copies: 6,
        available: 4,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400',
        description: 'One of the most inspiring and impactful books ever written, The 7 Habits of Highly Effective People has captivated readers for nearly three decades.',
        tags: ['Leadership', 'Personal Development', 'Success', 'Habits']
    },
    {
        id: 10,
        title: 'The Power of Now',
        author: 'Eckhart Tolle',
        isbn: '978-1577314806',
        publisher: 'New World Library',
        year: 1997,
        pages: 236,
        category: 'Self-Help',
        language: 'English',
        location: 'A-19-9',
        callNumber: '158.1 TOL',
        copies: 3,
        available: 3,
        status: 'available',
        image: 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400',
        description: 'To make the journey into the Now we will need to leave our analytical mind and its false created self, the ego, behind.',
        tags: ['Mindfulness', 'Spirituality', 'Present Moment', 'Consciousness']
    }
];

// Helper function to get book by ID
function getBookById(id) {
    return sampleBooks.find(book => book.id === parseInt(id));
}

// Helper function to filter books
function filterBooks(filters = {}) {
    let filtered = [...sampleBooks];

    if (filters.category) {
        filtered = filtered.filter(book => book.category === filters.category);
    }

    if (filters.status) {
        filtered = filtered.filter(book => book.status === filters.status);
    }

    if (filters.search) {
        const searchLower = filters.search.toLowerCase();
        filtered = filtered.filter(book => 
            book.title.toLowerCase().includes(searchLower) ||
            book.author.toLowerCase().includes(searchLower) ||
            book.isbn.includes(searchLower)
        );
    }

    return filtered;
}

// Helper function to get random books
function getRandomBooks(count = 6) {
    const shuffled = [...sampleBooks].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { sampleBooks, getBookById, filterBooks, getRandomBooks };
}
