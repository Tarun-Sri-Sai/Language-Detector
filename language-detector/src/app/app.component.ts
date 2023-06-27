import { Component } from '@angular/core'
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  textInput: string = ''
  result: string = ''
  private timeout: boolean = false

  constructor(private http: HttpClient) { }

  detectLanguage(): void {
    if (this.timeout) {
      console.log('Not running because of timeout')
      return
    }

    this.timeout = true

    if (!this.isValidLength()) {
      this.resetTimeout(1000)
      return
    }

    this.http.get<any>(`http://localhost:5000/detect-language?input_text=${this.textInput}`)
      .subscribe({
        next: (response) => {
          this.result = `This text is in ${response.language_code}`
        },
        error: (error) => {
          console.error('Error occurred during language detection:', error)
        }
      })

    this.resetTimeout(1000)
  }

  isValidLength(): boolean {
    return this.textInput.trim().replaceAll(/\s+/g, ' ').length >= 10
  }

  resetTimeout(delay: number): void {
    setTimeout(() => {
      this.timeout = false
    }, 1000)
  }
}