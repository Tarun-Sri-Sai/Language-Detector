import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root',
})
export class LanguageService {
    language: string = '';
    private timeout: boolean = false;
    private timeoutMillis: number = 500;

    constructor(private http: HttpClient) {}

    detectLanguage(textInput: string): void {
        if (this.timeout) {
            return;
        }
        this.timeout = true;
        this.makeRequest(textInput);
        this.resetTimeout();
    }

    makeRequest(textInput: string): void {
        this.http
            .post<any>('http://localhost:5000/language_detector/language', {
                text_input: textInput,
            })
            .subscribe({
                next: (response) => {
                    this.language = response['language_code'];
                },
                error: (error) => {
                    console.error("Couldn't compute language due to: ", error);
                },
            });
    }

    resetTimeout(): void {
        setTimeout(() => {
            this.timeout = false;
        }, this.timeoutMillis);
    }

    getLanguage(): string {
        return this.language;
    }
}
