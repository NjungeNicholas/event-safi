import React, { useState } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    { text: "Hi there! 👋 I'm your Event-Safi planning assistant. What type of event are you planning?", isUser: false }
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [vendors, setVendors] = useState([]);
  const [totalCost, setTotalCost] = useState(0);
  const [sessionId, setSessionId] = useState('');

  const sendMessage = async () => {
    if (!inputMessage.trim()) return;

    const userMessage = { text: inputMessage, isUser: true };
    setMessages(prev => [...prev, userMessage]);

    try {
      const response = await fetch('http://localhost:8000/api/chat/message/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          message: inputMessage,
          session_id: sessionId 
        })
      });

      const data = await response.json();
      
      const aiMessage = { text: data.response, isUser: false };
      setMessages(prev => [...prev, aiMessage]);
      
      if (data.vendors) {
        setVendors(data.vendors);
        setTotalCost(data.total_cost);
      }
      
      if (data.session_id) {
        setSessionId(data.session_id);
      }

    } catch (error) {
      console.error('Error:', error);
      const errorMessage = { text: "Sorry, I'm having trouble connecting. Please try again.", isUser: false };
      setMessages(prev => [...prev, errorMessage]);
    }

    setInputMessage('');
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div className="App">
      <header className="header">
        <h1>🎉 Event-Safi</h1>
        <p>Plan Any Event, Book Every Service — Effortlessly</p>
      </header>

      <div className="chat-container">
        <div className="messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.isUser ? 'user' : 'ai'}`}>
              <div className="message-content">
                {message.text}
              </div>
            </div>
          ))}
          
          {vendors.length > 0 && (
            <div className="vendors-section">
              <h3>🎯 Recommended Vendors</h3>
              <div className="vendors-grid">
                {vendors.map(vendor => (
                  <div key={vendor.id} className="vendor-card">
                    <div className="vendor-header">
                      <h4>{vendor.name}</h4>
                      <div className="rating">
                        ⭐ {vendor.rating}/5 ({vendor.reviews_count} reviews)
                      </div>
                    </div>
                    <p className="service-type">{vendor.service_type.toUpperCase()}</p>
                    <p className="portfolio">{vendor.portfolio}</p>
                    <p className="location">📍 {vendor.location}</p>
                    <div className="price">KES {vendor.price.toLocaleString()}</div>
                  </div>
                ))}
              </div>
              {totalCost > 0 && (
                <div className="total-cost">
                  <h3>Total Cost: KES {totalCost.toLocaleString()}</h3>
                  <button className="book-button">Confirm Booking</button>
                </div>
              )}
            </div>
          )}
        </div>

        <div className="input-section">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message here..."
            className="message-input"
          />
          <button onClick={sendMessage} className="send-button">
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
